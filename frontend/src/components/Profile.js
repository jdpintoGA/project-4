import React, { useState, useEffect } from 'react'
import axios from 'axios'
// import { Link } from 'react-router-dom'

import auth from '../lib/auth'

const Profile = () => {
  const [data, setData] = useState([])

  useEffect(() => {
    axios.get('/api/appointments/', { headers: { Authorization: `Bearer ${auth.getToken()}` } })
      .then((resp) => {
        setData(resp.data)

      })
  }, [])

  // console.log(data)
  return <div>

    {data.map(profile => {
      console.log(profile)
      return <div key={profile.id} className="column is-one-quarter-desktop is-one-third-tablet is-half-mobile">
        <div className="card">
          <div className="card-image">
            <figure className="image is-3by4">
              <img src={profile.user.image} alt="profile picture" />
            </figure>
          </div>

          <div id="file-button-center" className="file is-light is-danger">
            <label className="file-label">
              <input className="file-input" type="file" name="resume" />
              <span className="file-cta">
                <span className="file-icon">
                  <i className="fas fa-upload"></i>
                </span>
                <span className="file-label">
                  Edit Picture
                </span>
              </span>
            </label>
          </div>

          <div className="card-content has-text-centered">
            <h1>First Name: {profile.user.first_name}</h1>
            <h1>Last Name: {profile.user.last_name}</h1>
            <h1>Username: {profile.user.username}</h1>
            <h1>Age: {profile.user.age}</h1>
            <h1>Email: {profile.user.email}</h1>
            <h1>Phone Number: {profile.user.phone_number}</h1>
            <h1>Client Type: {profile.user.user_type}</h1>
          </div>

          <div className="field is-grouped">
            <p className="control">
              <button className="button is-success">
                Save changes
              </button>
            </p>
            <p className="control">
              <button className="button is-danger">
                Cancel
              </button>
            </p>
          </div>

        </div>
      </div>
    })}
  </div>

}

export default Profile