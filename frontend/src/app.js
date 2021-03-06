import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter, Switch, Route } from 'react-router-dom'
import 'bulma'
import './style.scss'

import Home from './components/Home'
import NavBar from './components/NavBar'
import Login from './components/Login'
import Register from './components/Register'
import Profile from './components/Profile'
import Services from './components/Services'
import Booking from './components/Booking'
import Footer from './components/Footer'

const App = () => (
  <HashRouter>
    <NavBar />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/register" component={Register} />
      <Route path="/login" component={Login} />
      <Route path="/profile" component={Profile} />
      <Route path="/services" component={Services} />
      <Route path="/bookings" component={Booking} />
    </Switch>
    <Footer />
  </HashRouter>
)

ReactDOM.render(<App />, document.getElementById('root'))
