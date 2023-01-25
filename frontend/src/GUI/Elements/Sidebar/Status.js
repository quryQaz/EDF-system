import React from 'react';
import { observer, inject } from 'mobx-react';
import styled from "styled-components";
import GetColorCode from 'Utils/GetColorCode'

const Cycle = styled.div`
    width: 10px;
    background-color: ${(props) => GetColorCode(props.color)};
    height: 10px;
    display: inline-block;
    border-radius: 50%;
    margin-top: 3px;
`

const Divider = styled.div`
    margin-left: 15px;
    vertical-align: middle;
    text-align: center;
    line-height: 20px;
    padding-top: 2px;
    padding-bottom: 2px;
    font-size: 16px;
`


export class Status extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
          <>
              <Cycle color={this.props.status == 'active' ? 'green' : 'red'}/>
              <Divider> | </Divider>
          </>
        )
    }

}
