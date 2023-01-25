import React from 'react';
import styled from "styled-components";
import {Header} from "GUI/Components/Dashboard/Pages/Components/Header"
import {Footer} from "GUI/Components/Dashboard/Pages/Components/Footer"
import {InfoAlert} from "GUI/Components/Dashboard/Pages/Components/InfoAlert"

const MainWrapper = styled.div`
    position: relative;
    width: 100%;
    height: 100%;
`

export class Alert extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        console.log(this.props.activeAlert);
        return(
            <MainWrapper>
                <Header label={`Alert ${this.props.activeAlert.ip}`}/>
                <InfoAlert alert={this.props.activeAlert}/>
                <Footer/>
            </MainWrapper>
        )
    }
}
