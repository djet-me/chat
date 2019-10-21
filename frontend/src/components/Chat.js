import React from 'react';
import PropTypes from 'prop-types';


const Chat = ({ data }) =>
  !data.length ? (
    <p>No messages yet</p>
  ) : (
    <div className='history'>
      {data.map(el => (
          <div key={el.id} className="message">
          <div className="pull-right">{ el['timestamp'] }</div>
          <div className="from-name">{ el['user'] }</div>
          <div className="text">{ el['text'] }</div>
        </div>
      ))}
    </div>
  );

Chat.propTypes = {
  data: PropTypes.array.isRequired
};

export default Chat;