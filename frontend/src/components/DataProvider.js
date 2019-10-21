import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { w3cwebsocket as W3CWebSocket } from 'websocket';

const client = new W3CWebSocket('ws://127.0.0.1:8000/ws/chat/');


class DataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  };

  state = {
    data: [],
    loaded: false,
    placeholder: 'Loading...'
  };

  componentDidMount() {
    fetch(this.props.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong. Please try again later."});
        }
        return response.json();
      })
      .then(data => {
        this.setState({ data: data, loaded: true});
        let historyDiv = document.getElementsByClassName("history")[0];
        if (historyDiv) {
          historyDiv.scrollTop = historyDiv.scrollHeight;
        }
      });

    client.onopen = () => {
      console.log('New Client Connected');
    };
    client.onmessage = (message) => {
      this.setState({data: [...this.state.data, JSON.parse(message.data)['message']]});
      let historyDiv = document.getElementsByClassName("history")[0];
      if (historyDiv) {
        historyDiv.scrollTop = historyDiv.scrollHeight;
      }
    };
  }

  render() {
    const {data, loaded, placeholder } = this.state;
    return loaded ?this.props.render(data): <p>{ placeholder }</p>;
  }
}

export default DataProvider;