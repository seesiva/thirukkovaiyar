import React, { Component } from 'react';

// Import Components
import Header  from './components/Header/header'
import HomePage  from './components/Pages/homepage'
import Footer  from './components/Footer/footer'

// Import assets
import './Assets/css/default.min.css'


class App extends Component {
  render() {
    return (
      <div className="App">
        <Header/>
        <HomePage/>
        <Footer/>
      </div>
    );
  }
}

export default App;
