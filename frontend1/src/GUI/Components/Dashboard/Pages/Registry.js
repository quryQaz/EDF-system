import React from 'react';
import styled from "styled-components";
import {Header} from "GUI/Components/Dashboard/Pages/Components/Header"
import {Footer} from "GUI/Components/Dashboard/Pages/Components/Footer"
import {Info} from "GUI/Components/Dashboard/Pages/Components/Info"
import {basicRequestPost} from "MODELS/Requests/basicRequestPost"
import {config} from "Utils/Config"
import { observable, action, makeObservable } from "mobx";
import { observer } from "mobx-react";


const MainWrapper = styled.div`
    position: relative;
    width: 100%;
    height: 100%;
`

const Registry = (observer(class extends React.Component {

    items = []

    constructor(props) {
        super(props);
        makeObservable(this, {
          items: observable,
          setItems: action
        });
        this.loadData();
    }

    setItems = (data) => this.items = data;

    loadData = () => {
        basicRequestPost(`${config.BACKEND_URL}/api/registry`, {ip: this.props.ip}).then((response) => {
            this.setItems(response.data.data);
            console.log(this.items);
        })
    }

    render() {
        return(
            <MainWrapper>
                <Header label={"System information"}/>
                <Info items={this.items}/>
                <Footer/>
            </MainWrapper>
        )
    }
}));

export default function(props) {
  return <Registry {...props} />;
}
