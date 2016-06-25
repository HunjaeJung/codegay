var createHistory = require('history').createHistory

var history = createHistory()

// Get the current location.
const location = history.getCurrentLocation()

// Listen for changes to the current location.
const unlisten = history.listen(location => {
  console.log(location.pathname)
})

// When you're finished, stop the listener.
unlisten()
