import React from "react";
import styled from "styled-components";
import Sidebar from "GUI/Elements/Sidebar"
import Alerts from "GUI/Components/Dashboard/Alerts"
import {getPages} from "GUI/Components/Dashboard/PagesList"
import {DefaultPage} from "GUI/Components/Dashboard/Pages/DefaultPage"
import {basicRequestGet} from "MODELS/Requests/basicRequestGet"
import {config} from "Utils/Config"
import { observable, action, makeObservable } from "mobx";
import { observer } from "mobx-react";


const MainFormWrapper = styled.div`
    width: 100%;
    height: 100vh;
    display: flex;
    position: absolute;
`

const PageWrapper = styled.div`
    height: 100%;
    padding-left: 330px;
    padding-right: 300px;
    width: 100%;
    background: rgb(0,0,0);
    background: linear-gradient(90deg, rgba(15,15,15,1) 0%, rgba(20,20,20,1) 50%, rgba(40,40,40,1) 100%);
`
// background-color: #1e1e1e;
// background-image: url('https://uploads-ssl.webflow.com/5a9ee6416e90d20001b20038/635ac0a24a485ff0387c8448_horizontal%20(19).svg');

const AlertWrapper = styled.div`
    height: 100%;
    position: fixed;
    right: 0px;
    width: 300px;
    background-image: url('https://stonexpo.ru/upload/iblock/ad9/Starlight_Black_1.jpg');
`
const Dashboard = (observer(class extends React.Component {

    defaultState = {
      activeTab : -1,
      activeIp : null,
      alertsOpen: false,
      MLActive: false
    };

    alerts = []

    constructor(props) {
        super(props);
        document.title = "Dashboard";
        this.state = this.defaultState;
        makeObservable(this, {
          alerts: observable,
          setAlerts: action
        });
    }

    setAlerts = (data) => this.alerts = data;
    changeMLState = () => {
        this.setState({ MLActive : !this.state.MLActive });
    }

    loadAlerts = () => {
        basicRequestGet(`${config.BACKEND_URL}/api/alerts`).then((response) => {
            this.setAlerts(response.data.data);
            console.log(this.alerts);
        })
    }

    pages = getPages();

    changeTab = newIndex => this.setState({ activeTab : newIndex });
    changeIp = newIp => this.setState({ activeIp : newIp });
    changeActiveAlertState = newAlert => this.setState({activeAlert: newAlert})

    changeAlertsState = () => {
        this.setState({ alertsOpen : !this.state.alertsOpen });
    }

    setAlertsState = (state) => {
        this.setState({ alertsOpen : state });
    }

    renderPage = (index) => {
        if (index < 0) {
            return (<DefaultPage/>)
        }

        const Page = this.pages[index].component;

        return (
            <Page
                ip={this.state.activeIp}
                activeAlert={this.state.activeAlert ? this.state.activeAlert : null}
                MLActive={this.state.MLActive}
            />
        )
    }

    render() {
        return (
            <MainFormWrapper>
                <Sidebar
                    changeTab={this.changeTab}
                    changeIp={this.changeIp}
                    loadAlerts={this.loadAlerts}
                    setAlertsState={this.setAlertsState}
                    changeMLState={this.changeMLState}
                    MLActive={this.state.MLActive}
                />
                <PageWrapper>
                    { this.renderPage(this.state.activeTab) }
                </PageWrapper>

                <AlertWrapper>
                    <Alerts
                        items={this.alerts}
                        changeAlertsState={this.changeAlertsState}
                        isActive={this.state.alertsOpen}
                        changeTab={this.changeTab}
                        changeActiveAlertState={this.changeActiveAlertState}
                    />
                </AlertWrapper>
            </MainFormWrapper>
        )
    }

}));

export default function(props) {
  return <Dashboard {...props} />;
}
