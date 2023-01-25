import React from 'react';
import styled from "styled-components";
import {Header} from "GUI/Components/Dashboard/Pages/Components/Header"
import {Footer} from "GUI/Components/Dashboard/Pages/Components/Footer"

const MainWrapper = styled.div`
    position: relative;
    width: 100%;
    height: 100%;
`

const MessageWrapper = styled.div`
    color: white;
    font: small-caps bold 30px/1 sans-serif;
    margin-top: 35%;
    padding-left: 20px;
`

export class DefaultPage extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <MainWrapper>
                <Header label={"Default Page"}/>
                    <MessageWrapper>
                        Выберите сервер, который хотите посмотреть
                    </MessageWrapper>
                <Footer/>
            </MainWrapper>
        )
    }
}
