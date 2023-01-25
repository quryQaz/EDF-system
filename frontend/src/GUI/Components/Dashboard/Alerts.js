import React from 'react';
import styled from "styled-components";
import Arrow from "styles/icons/arrow"
import Menu from "styles/icons/menu"
import ButtonWithIcon from "GUI/Elements/Buttons/ButtonWithIcon"
import Button from "GUI/Elements/Buttons"
import { StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native-web';
import {basicRequestPost} from "MODELS/Requests/basicRequestPost"
import {config} from "Utils/Config"
import { observable, action, makeObservable } from "mobx";
import { observer } from "mobx-react";
import "styles/alerts.css"

const ComponentWrapper = styled.div`
    margin: 0px;
    height: 100%;
    padding-top: 10px;
    position: relative;
`

const MainWrapper = styled.div`
    position: relative;
    height: 100%;
    width: 100%;
`

const TitleHeader = styled.div`
    width: 105px;
    height: 50px;
    padding: 0px 20px;
    margin: 5px 55px;
    font: small-caps bold 30px/1 sans-serif;
    color: white;
    float: left;
    border-bottom: 1px ridge white;
`

const ButtonWrapper = styled.div`
    width: 40px;
    float: left;
`

const ContentWrapper = styled.div`
    width: 100%;
    height: calc(100% - 115px);
    margin-top: 15px;
    margin-left: 30px;
`

const Alerts = (observer(class extends React.Component {

    constructor(props) {
        super(props);
    }

    clickAlert = (alert) => {
        this.props.changeActiveAlertState(alert);
        this.props.changeTab(8)
    }

    render() {
        return(
            <MainWrapper>
                <ComponentWrapper className={this.props.isActive ? "alerts-active" : "alerts"}>
                    <ButtonWrapper>
                        <ButtonWithIcon
                        label={''}
                        backgroundColorRGB={'rgba(21,21,21,1)'}
                        borderColor={'white'}
                        width={'35px'}
                        height={'35px'}
                        fontSize={'20px'}
                        borderRadius={'10px'}
                        margin={'0px 10px'}
                        icon={<Menu/>}
                        innerPadding={'0px 0px 0px 5px'}
                        onClick={this.props.changeAlertsState}
                        />
                    </ButtonWrapper>
                    <TitleHeader>
                    Alerts
                    </TitleHeader>
                    <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
                        { this.props.isActive &&
                              <ContentWrapper>
                                {this.props.items.map((alert, i) => {
                                    return (
                                    <ButtonWithIcon
                                        label={`Detected ${alert.ip}`}
                                        key={i}
                                        backgroundColorRGB={'rgba(21,21,21,1)'}
                                        borderColor={'white'}
                                        width={'240px'}
                                        height={'35px'}
                                        fontSize={'20px'}
                                        borderRadius={'10px'}
                                        margin={'15px 0px'}
                                        innerPadding={'0px 10px 0px 5px'}
                                        onClick={() => this.clickAlert(alert)}
                                    />
                                    )
                                })}
                            </ContentWrapper>
                        }
                    </ScrollView>
                </ComponentWrapper>
            </MainWrapper>
        )
    }
}));

const styles = StyleSheet.create({
  scrollView: {
    height: '100%',
    width: '100%',
  }
});

export default function(props) {
  return <Alerts {...props} />;
}


const test = [
    {
        ipFrom: "192.168.1.2",
        date: "03.03.2022 09:00",
        log: "log alert 192.52.23.21",
        ip: "192.52.23.21"
    },
    {
        ipFrom: "192.168.1.3",
        date: "03.02.2022 09:00",
        log: "log alert 192.57.23.22",
        ip: "192.57.23.22"
    },
    {
        ipFrom: "192.168.1.4",
        date: "04.08.2022 10:00",
        log: "log alert 197.54.23.24",
        ip: "197.54.23.24"
    },
]
