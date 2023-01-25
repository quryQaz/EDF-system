import React from 'react';
import styled from "styled-components";
import { StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native-web';

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

export class InfoLogs extends React.Component {

    constructor(props) {
        super(props);
    }

    getColor = () => {
        if (this.props.MLActive)
            return Math.floor(Math.random() * 2) == 1 ? 'orange' : '';
        return '';
    }

    makeInfoRow = (data, index) => {
        return(
            <RowWrapper key={index} style={{color: this.getColor()}}>
                <b style={{color: '#a6a6a6'}}>
                    {index+1}
                </b>
                &nbsp;|&nbsp;
                {data.date}
                <br/>
                {data.data}
            </RowWrapper>
        )
    }

    render() {
      return (
          <MainWrapper>
              <InfoWrapper>
                  <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
                    <Text style={styles.text}>
                        {this.props.items.map((data, index) => this.makeInfoRow(data, index))}
                    </Text>
                  </ScrollView>
              </InfoWrapper>
          </MainWrapper>
      );
    }
}

const styles = StyleSheet.create({
  scrollView: {
    height: '100%',
    marginHorizontal: 15,
    width: '100%',
  },
  text: {
    fontSize: 16,
    color: 'white',
  },
});
