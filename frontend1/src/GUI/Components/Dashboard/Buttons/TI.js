import React from 'react';
import styled from "styled-components";

const ButtonsWrapper = styled.div`
    margin: 0px;
    height: 5%;
    background-color: green;
`

export class Buttons extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <ButtonsWrapper>
                Buttons
            </ButtonsWrapper>
        )
    }
}
