import React from 'react';
import styled from "styled-components";
import {Header} from "GUI/Components/Dashboard/Pages/Components/Header"
import {Footer} from "GUI/Components/Dashboard/Pages/Components/Footer"
import ConsoleMain from "GUI/Components/Dashboard/Pages/Components/Console"

const MainWrapper = styled.div`
    position: relative;
    width: 100%;
    height: 100%;
`

export class Console extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <MainWrapper>
                <Header label={'Console'}/>
                    <ConsoleMain ip={this.props.ip}/>
                <Footer/>
            </MainWrapper>
        )
    }
}
