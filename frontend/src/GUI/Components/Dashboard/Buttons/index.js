import React from 'react';
import styled from "styled-components";
import ButtonWithIcon from "GUI/Elements/Buttons/ButtonWithIcon"
import ML from "styles/icons/ML"
import TI from "styles/icons/TI"

const ButtonsWrapper = styled.div`
    margin: 0px;
    height: 5%;
    display: flex;
`

const IconWrapper = styled.div`
`

export class Buttons extends React.Component {

    constructor(props) {
        super(props);
    }

    makeIcon = (icon) => {
        return (
            <IconWrapper>
                {icon}
            </IconWrapper>
        )
    }

    clickTI = () => {
      this.props.loadAlerts();
      this.props.setAlertsState(true);
    }

    render() {
        return(
            <ButtonsWrapper>
                <ButtonWithIcon
                    label={'ML'}
                    backgroundColorRGB={'rgba(21,21,21,0.8)'}
                    width={'150px'}
                    height={'60%'}
                    fontSize={'20px'}
                    borderRadius={'10px'}
                    margin={'5px 10px'}
                    icon={this.makeIcon(<ML/>)}
                    borderColor={this.props.MLActive ? 'green' : 'white'}
                    padding={'0px'}
                    onClick={this.props.changeMLState}
                />
                <ButtonWithIcon
                    label={'TI'}
                    backgroundColorRGB={'rgba(21,21,21,0.8)'}
                    borderColor={'white'}
                    width={'150px'}
                    height={'60%'}
                    fontSize={'20px'}
                    borderRadius={'10px'}
                    margin={'5px 10px'}
                    icon={this.makeIcon(<TI/>)}
                    onClick={this.clickTI}
                />
            </ButtonsWrapper>
        )
    }
}
