const express = require('express')

const app = express()

app.all('/', (req, res) => {

    console.log("Just got a request!")

    res.send('Yo! i am Made By My Master')

})

app.listen(process.env.PORT || 8000)
