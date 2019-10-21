import React from 'react';
import ReactDOM from 'react-dom';
import DataProvider from "./DataProvider";
import Chat from "./Chat";
import MessageForm from "./MessageForm";


const App = () => (
  <React.Fragment>
    <div className="page-wrap">
      <div className="page-body chat-page">
        <DataProvider endpoint='/api/v1/messages/messages/' render={data =>
          <Chat data={data} />
        } />
        <MessageForm endpoint='/api/v1/messages/messages/' />
      </div>
    </div>
  </React.Fragment>
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper): null;