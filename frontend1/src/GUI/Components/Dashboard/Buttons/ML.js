import React from 'react';
import styled from "styled-components";
import {Button} from "GUI/Elements/Buttons"

const ButtonsWrapper = styled.div`
    margin: 0px;
    height: 5%;
    background-color: green;
`

export class ML extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <ButtonsWrapper>
                <Button
                    lable={'ML'}
                    backgroundColor={'black'}
                    width={'30%'}
                    borderRadius={'0px'}
                    
                />
            </ButtonsWrapper>
        )
    }
}
