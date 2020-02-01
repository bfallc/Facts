console.log("bot working");

var Twit = require('twit');

var config = require('./config');
console.log(config);
var T = new Twit(config);

//
//  filter the twitter public stream by the word 'mango'.
//
var stream = T.stream('statuses/filter', { track: 'the fact' })
 
stream.on('tweet', function (tweet) {
  console.log(tweet['text']);
    console.log(tweet['created_at']);
    console.log('next');
})
 