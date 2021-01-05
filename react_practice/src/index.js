import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App'; // App을 import해서 쓴다.
import reportWebVitals from './reportWebVitals';

// public/index.html의 id가 root인 곳에 App을 렌더링해서 넣는다.
// document의 root 부분을 React.StrictMode로 렌더링하겠다.
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
