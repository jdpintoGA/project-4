# project-4
SEI Group Project

### ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) General Assembly, Software Engineering Immersive
# Laboratory Appointment Booking System - LABS
​
## Overview
​
​
LABS is a full-stack app which was done in a group of four. We used React in the front end and Django in the back end.
The concept of this project was to build a boooking platform for an actual bussines where they will get an MVP demo version to be implemented in the future when it will be fully functional.

​
You can launch the site on Heroku [here](https://labs-project4.herokuapp.com/#/) 
​
## The Brief 
​
- **Build a full-stack application by making your own backend and your own front-end**
- **Use a Python Django API using Django REST Framework to serve your data from a PostgreSQL database**
- **Consume your API with a separate front-end built with React**  
- **Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models** 
- **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut** 
- **Have a visually impressive design to kick your portfolio up a notch and have something to wow future clients & employers. ALLOW time for this**
​
​
## The Technologies used 
​
- HTML5
- CSS3
- JavaScript(ES6+)
- React.js
- Python
- Django
- Insomnia
- Bulma
- Webpack
- JSON
- Babel
- Google Fonts
- SASS
- Heroku
- Git and GitHub
- LoaderSpinner

​
​
## The Approach 
​
​
We started by defining the data models.
​
<img  src=frontend/images/relationships.png height=500> 
 
 As we can observe in the picture above we have four modules with their porperties what will build the relationship betwen them. 
​
 `categories`, `services` and `appointemnt` are in the apointments app and the `user` is used for the Authorization with jwt library.

​
 **RELATIONSHIPS**
​
 User id -----> Appoitments User
    (one to many)

​
Appointments services ------> Services id
                  (many to many)

​
 Categories id  -----> Services category
               (one to many )

​
​
​
We did not use any external API as we have created our own fixture file taking advantage of the fact that we could use the Django Framework. 229 services provided by the healthcare institution  were hardcoded in the framework and then a fixture file with all the avaliable services, so when we were loading the databases is worth to mention that was done with Postgree SQL database as it was the first time that we have the chance to work during the project with SQL.
​
​
<img  src=frontend/images/PostgreeSQL.png height=500> 
​
 
​
## The Backend
​
​
**Models**

​
Because Django gives a user model built in, we extend it with aditonal field that were required.
​
`age`
​
`phone-number`
​
Built in fields for the user in django
​
`email`
​
`id`
​
`username`
​
`firstname`
​
`lastname`
​
`password`
​
`password-confirmation`
​
​
example of a User model
```js
class User(AbstractUser):
    age = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    BUSINESS = 'BA'
    INDIVIDUAL = 'IN'
    USER_TYPE_CHOICES = [
        (BUSINESS, 'Business'),
        (INDIVIDUAL, 'Individual'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=INDIVIDUAL,
    )
​
    def __str__(self):
        return self.username
​
```
​
we have an aditional field called `User_type` as it was one of our strech goals for the project what needs to be done.
​

**Serializers**
​

Each model has their own serializer
​
`AppointmentSerializer`
​
`CategorySerializer`
​
`ServiceSerializer`
​
`UserSerializer`
​
​
```js
​
class AppointmentSerializer(serializers.ModelSerializer):
​
    class Meta:
        model = Appointment
        fields = ('id', 'appointment_date', 'services', 'user')
        extra_kwargs = {
            'services': {'required': False}
        }
```
​
​
And then we were building the relationships between them with the following serializers.
​
`PopulateServiceSerializer`
​
`PopulateCategorySerializer`
​
`PopulateAppointmentSerializer`
​
​
​
```js
​
​
class PopulateAppointmentSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    user = UserSerializer()
​
    class Meta:
        model = Appointment
        fields = ('id', 'appointment_date', 'user', 'services')
​
```
​
**Views**

​
We generate different views in order to get the information passed from our serializers previously as a part of our MVC.
​
​
`ListView(APIView)`
​
`DetailView(RetrieveUpdateDestroyAPIView)`
​
`ServiceListView(ListCreateAPIView)`
​
`ServiceDetailView(RetrieveUpdateDestroyAPIView)`
​
`CategoryListView(ListCreateAPIView)`
​
`CategoryDetailView(RetrieveUpdateDestroyAPIView)`
​
`UserDetailView(RetrieveUpdateDestroyAPIView)`
​
​
As an example we look at ListView which is the main view we were using in order to get the list of appointments with their relationship to the user and catergory with their services.
​
​
​
```js
class ListView(APIView):  # extend the APIView
    permission_classes = (IsAuthenticated, )
​
    def get(self, _request):
        current_user = request.user.id
        appointment = Appointment.objects.all()
        serializer = PopulateAppointmentSerializer(appointment, many=True)
​
        return Response(serializer.data)  # send the JSON to the client
​
​
```
​
​
**The Endpoints**

We had 8 endpoints as listed below:
​
```js
    path('', ListView.as_view()),
    path('appointments/', ListView.as_view()),
    path('<int:pk>/', DetailView.as_view()),
    path('services/', ServiceListView.as_view()),
    path('services/<int:pk>/', ServiceDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
​
```
​
​
​
​
​
## The Front-End
​
It was built using React Classes and Hooks, containing 11 components which we were used to construct the front-end. We will list below and talk about the most relevant.
​
<img  src=frontend/images/labs.png height=500>
​
`Register.js` and `Login.js`
​
We built a standard Register and Login form where we will be validating the user with their tokens. 
​
The information entered by the user in the registration and login forms is set as state and then posted to our backend endpoints through  `/api/register` and `/api/login`. 
​
`Service.js`, `ServiceCard.js` and `Dropbox.js`
​
​
We first have created a `Dropbox.js` component that will be listing the different categories and rendering into the `Service.js`. We created  `hadleDropDown()` function which filters the event selected in the `Dropbox.js`. If the user selects, 'Search All', it will return all the services, if the user selects one category, that catergory is converted to lowecase which matches the event clicked. Hence, returning only the selected category in the form of card that is built into the `ServicesCard.js` component.
​
```js
  componentDidMount() {
    axios
      .get('/api/appointments/category/')
      .then((res) => {
        this.setState({
          category: res.data,
          filteredCategories: res.data
        })
      })
      .catch((error) => console.error(error))
  }
​
  handleDropdown(event) {
    this.setState({ dropDownOption: event.target.value })
​
    if (event.target.value === 'Search All') {
      this.setState({ filteredCategories: this.state.category })
    } else {
      const onlyDropdownSelected = this.state.category.filter((service) => {
        if (
          service.category.toLowerCase() === event.target.value.toLowerCase()
        ) {
          return event.target.value
        }
      })
      this.setState({ filteredCategories: onlyDropdownSelected })
    }
  }
​
  handleChange(event) {
    const choices = this.state.choices
​
    if (event.target.checked === true) {
      choices.push(event.target.value)
      console.log(choices)
      this.setState({ choices })
    } else {
      const newchoices = choices.filter((choice) => {
        return choice !== event.target.value
      })
      this.setState({ choices: newchoices })
    }
  }
​
​
```
​
`Booking.js`
​
The state from `Service.js` is passed to `Booking.js` with the previously selected services. 
​
​
```js
              <Link
                to={{
                  pathname: '/bookings',
                  state: this.state.choices
                }}
​
```
​
As we were passing the state in the form of an array, we had to transform it back to an object in order to render all the required information. 
​
​
```js
componentDidMount() {
    const testArray = this.props.location.state.map((serviceObject) => {
      return JSON.parse(serviceObject)
    })
​
```
​
Once we are getting the information we are mapping through the passed state and redering all the selected services for the booking.
​
By using a reduce function, we are summing the total amount to be paid 
​
​
```js
              {mappedAppointments.reduce((acc, element) => {
                return acc + parseFloat(element.private_price)
              }, 0)}
​
```
​
​
Finally, we had to select a time and date for our appointment, all this will then be posted to our backend endpoint `/api/appointments/`.
​
​
```js
  handleSubmit(event) {
    event.preventDefault()
​
    axios
      .post('/api/appointments/', this.state.data, {
        headers: { Authorization: `Bearer ${auth.getToken()}` }
      })
      .then(console.log('POST IS DONE'))
      .then((res) => {
        this.props.history.push('/profile')
      })
      .catch((error) => console.error(error))
  }
​
```
​
`Profile.js`
​
In the Profile component, we are using React Hooks for learning purposes, where instead of using a `ComponentDidMount()` function to use the get method, now we will be using `useEffect()` function what is built in with the Hooks.
​
By calling our Axios method, we are geting the profile information from the logged in user which corresponds to an authorization token. We will gather just the fields from the user model that is logged in.
​
```js
  useEffect(() => {
    axios
      .get('/api/profile', {
        headers: { Authorization: `Bearer ${auth.getToken()}` }
      })
      .then((resp) => {
        setData(resp.data)
        // console.log(data)
      })
      .catch((error) => console.error(error))
  }, [])
​
​
```
​
This component is the last one of the User journey as it will be showing all the appointments for the particular user.
​
<img  src=frontend/images/profile.png height=500>
​
​
## Challenges
​
- When trying to pass the state from `Services.js` to `Booking.js` it was challeging due to the fact that we were passing an array of strings and what we actually need was an object to be passed. We spent several hours for the solution. Later we got to the conclussion that before transforming to an object we must map through this array of string and use `JSON.parse()` method.
​
- When building the data modeling at the begining of the project we didn't consider the amount of time that will consume to construct such application. So we had to get rid of some functionalities that we wanted to implement in the beginning such as locations for the health care institution where to book the appointment and the implementation of another kind of user as a B2B. So that's why we have created two different user_type in the beginning.
​
- Trying to create the Populate serializers for some of the views was a challenge. As our models didn’t always have the information required for some of the views that we wanted to create, we had to create populated serializers that would allow us to display the information in the format that we needed.  Getting this correct was not simple, given the relationships between some of the models.
​
​
 ## Successes
​
 - One big success was planning at the beginning of the project, when doing the data modeling we had a clear idea of what we wanted to build so the MVC was achieved in a fast and efficient manner. 