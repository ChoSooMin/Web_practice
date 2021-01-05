// import logo from './logo.svg';
// import './App.css';
import Hello from './component/Hello'; // 내가 만든 컴포넌트를 쉽게 사용하려면 import Hello 해야한다.

function App() {
  return (
    // 브라우저가 해석해야하는 부분 (JSX 문법)
    // 반드시 root element는 있어야 한다.
    <div className="App">
      <Hello />
    </div>
  );
}

export default App; // export를 해야 다른 데에서 import를 할 수 ㅇㅆ다.
