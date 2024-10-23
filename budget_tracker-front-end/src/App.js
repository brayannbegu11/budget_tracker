import logo from './logo.svg';
import './App.css';
import { Route, Router, Switch } from 'react-router-dom';
import { Login } from './pages/Login';

function App() {
  return (
    <Router>
      <Switch>
        <Route path='/login' Component={Login} />
      </Switch>
    </Router>
  );
}

export default App;
