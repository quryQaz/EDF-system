import React from 'react';
import styled from "styled-components";
import { StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native-web';
import Input from "GUI/Elements/Input"
import { observable, action, makeObservable } from "mobx";
import { observer } from "mobx-react";
import {config} from "Utils/Config"
import {basicRequestPost} from "MODELS/Requests/basicRequestPost"

const MainWrapper = styled.div`
    width: calc(100% - 20px);
    height: calc(100% - 91px);
    font: small-caps bold 15px/1 sans-serif;
    color: white;
    padding: 0px 10px;
`

const InfoWrapper = styled.div`
    width: 100%;
    height: 100%;
    border-left: 1px ridge white;
    border-right: 1px ridge white;
`

const RowWrapper = styled.div`

    padding-bottom: 5px;
    width: 95%;
    margin-right: 20px;
    margin-bottom: 5px;
    word-break: break-all;
`

const InputWrapper = styled.div`
    margin: 10px 30px;
    width: calc(100% - 60px);
    border-bottom: 1px solid white;
`

const PreInputWrapper = styled.div`
    display: inline-block;
    margin-right: 5px;
`


const ConsoleMain = (observer(class extends React.Component {

    inputValue = ""
    log = []

    constructor(props) {
        super(props);
        makeObservable(this, {
          inputValue: observable,
          valueChange: action,
          log: observable,
          addLog: action
        }
        );
    }

    valueChange = (value) => {this.inputValue = value};
    addLog = (value) => {this.log.push(value)};

    makeInfoRow = (data, index) => {
        return(
            <RowWrapper key={index}>
                <b style={{color: '#a6a6a6'}}>
                    {data.command}
                </b>
                &nbsp;|&nbsp;
                <br/>
                {data.output}
            </RowWrapper>
        )
    }

    sendCommand = (command) => {
        this.inputValue = ""
        basicRequestPost(`${config.BACKEND_URL}/api/console`, {ip: this.props.ip, command: command}).then((response) => {
            this.addLog(response.data.data);
            console.log(response.data);
        }).catch((response) => {
            console.log(response);
            this.addLog({
                command: command,
                output: response.response.data.message
            });
        })
    }

    handleKeyDown = () => {
        if (event.key === 'Enter') {
            this.sendCommand(this.inputValue)
            console.log(this.inputValue);
        }
    }

    onChangeInputValue = (value = "") => {
        this.valueChange(value);
    }

    render() {
      console.log(this.log);
      return (
          <MainWrapper>
              <InfoWrapper>
                  <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
                    <Text style={styles.text}>
                        {this.log.map((data, index) => this.makeInfoRow(data, index))}
                    </Text>
                  </ScrollView>
                  <InputWrapper>
                      <PreInputWrapper>
                          {'>'}
                      </PreInputWrapper>
                      <Input
                          margin={"0px"}
                          value={this.inputValue}
                          mainWidth={"95%"}
                          onChange={this.onChangeInputValue}
                          handleKeyDown={this.handleKeyDown}
                      />
                  </InputWrapper>
              </InfoWrapper>
          </MainWrapper>
      );
    }
}));

export default function(props) {
  return <ConsoleMain {...props} />;
}

const styles = StyleSheet.create({
  scrollView: {
    height: '93%',
    marginHorizontal: 15,
    width: '100%',
  },
  text: {
    fontSize: 16,
    color: 'white',
  },
});

const test = [
  {command: 'ls', date: '21.02.2022 08:22:22', output: "t t t tt t t t t "},
  {command: 'cat test123', date: '21.02.2022 08:22:22', output: "test321"},
  {command: 'ps', date: '21.02.2022 08:22:22', output: "ssdd safa wawra awr r arwar "},
  {command: 'whoami', date: '21.02.2022 08:22:22', output: "test321"},
  {command: 'ttt', date: '21.02.2022 08:22:22', output: "rrr"},
]
