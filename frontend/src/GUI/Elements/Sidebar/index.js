import React from 'react';
import { observer, inject } from 'mobx-react';
import styled from "styled-components";

import 'styles/sidebar.css';
import {Navigation} from 'react-minimal-side-navigation';
import GetColorCode from 'Utils/GetColorCode'
import {defaultSubNav} from 'GUI/Elements/Sidebar/defaultSubNav'
import {Status} from 'GUI/Elements/Sidebar/Status'
import Dashboard from 'styles/icons/dashboard'
import {Buttons} from "GUI/Components/Dashboard/Buttons"
import {basicRequestPost} from "MODELS/Requests/basicRequestPost"
import {basicRequestGet} from "MODELS/Requests/basicRequestGet"
import {config} from "Utils/Config"
import { observable, action, makeObservable } from "mobx";
import { observer } from "mobx-react";


const SidebarWrapper = styled.div`
    position: fixed;
    width: 330px;
    background-color: ${GetColorCode('white')};
    background-image: url('https://stonexpo.ru/upload/iblock/ad9/Starlight_Black_1.jpg');
    display: block;
    height: 100%;
`

const SidebarHeader = styled.div`
    width: 100%;
    height: 100px;
    padding-left: 20px;
    padding-top: 30px;
    font: small-caps bold 30px/1 sans-serif;
    color: white;
`

const ButtonsWrapper = styled.div`
    bottom: 0px;
    width: 100%;
    position: absolute;
`

const NavigationWrapper = styled.div`
    bottom: 0px;
    width: 100%;
`


const Sidebar = (observer(class extends React.Component {

    items = []

    constructor(props) {
        super(props);
        makeObservable(this, {
          items: observable,
          setItems: action
        });
        this.loadData();
    };

    setItems = (data) => this.items = data;

    loadData = () => {
        basicRequestGet(`${config.BACKEND_URL}/api/statuses`).then((response) => {
            this.setItems(response.data.data);
            console.log(this.items);
        })
    }

    makeItems = (items) => {
        return items.map(item => {
            return {
              title: item.ip,
              itemId: item.ip,
              subNav: defaultSubNav(item.ip),
              elemBefore: () => <Status status={item.status}/>
            }
        })
    }

    onDisconnect = (ip) => {
        basicRequestPost(`${config.BACKEND_URL}/api/actions/disconnect`, {ip: ip}).then(this.loadData);
    }

    onClear = (ip) => {
        basicRequestPost(`${config.BACKEND_URL}/api/actions/clear`, {ip: ip}).then(this.loadData);
    }

    onSelect = (itemId) => {
        console.log(itemId);
        const {changeTab, changeIp} = this.props;

        const item = itemId.itemId.split('/');
        if (item.length == 2) {
            switch (item[1]) {
                case "Drivers":
                  changeTab(0)
                  break;
                case "Processes":
                  changeTab(1)
                  break;
                case "Registry":
                  changeTab(2)
                  break;
                case "Logs":
                  changeTab(3)
                  break;
                case "Errors":
                  changeTab(4)
                  break;
                case "Programs":
                  changeTab(5)
                  break;
                case "Users":
                  changeTab(6)
                  break;
                case "Console":
                  changeTab(7)
                  break
                case "Disconnecs":
                  this.onDisconnect(item[0]);
                  break;
                case "Clear":
                  this.onClear(item[0]);
                  break;
                default:
                  break;
            }
            changeIp(item[0])
        }
    }

    render() {

        return (
            <SidebarWrapper>
                <SidebarHeader>
                    EDR Dashboard
                </SidebarHeader>
                <NavigationWrapper>
                    <Navigation
                        onSelect={this.onSelect}
                        items={this.makeItems(this.items)}
                    />
                </NavigationWrapper>
                <ButtonsWrapper>
                    <Buttons
                        loadAlerts={this.props.loadAlerts}
                        setAlertsState={this.props.setAlertsState}
                        changeMLState={this.props.changeMLState}
                        MLActive={this.props.MLActive}/>
                </ButtonsWrapper>
            </SidebarWrapper>
        )
    }

}));

export default function(props) {
  return <Sidebar {...props} />;
}
