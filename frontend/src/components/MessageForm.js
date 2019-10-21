import React, { Component } from 'react';
import PropTypes from 'prop-types';


class MessageForm extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired
  };

  state = {
    text: ''
  };

  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = e => {
    e.preventDefault();
    const { text } = this.state;
    const message = { text };
    this.setState({
      text: ''
    });
    const conf = {
      method: 'post',
      body: JSON.stringify(message),
      headers: new Headers({ "Content-Type": "application/json"})
    };
    fetch(this.props.endpoint, conf).then(response => console.log(response));
  };

  render() {
    const { text } = this.state;
    return (
      <div className='message-input'>
        <form onSubmit={this.handleSubmit}>
          <input type="text" name="text" onChange={this.handleChange} value={ text } required />
          <button type='submit'>Send</button>
        </form>
      </div>
    );
  }
}

export default MessageForm;
