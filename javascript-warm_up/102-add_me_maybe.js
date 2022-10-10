#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
    number = number + 1;
    theFunction(number)
}

// const ddMeMaybe = require('./102-add_me_maybe').addMeMaybe;
// addMeMaybe(4, function (nb) {
//   console.log('New value: ' + nb);
// });