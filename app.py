const request = require('request');
const cheerio = require('cheerio');
const moment = require('moment');

const jsdom = require("jsdom");
const { JSDOM } = jsdom;

var data = {
  FromCity: 9,
  FromStation: 1239,
  FromStationName: 0,
  ToCity: 18,
  ToStation: 5102,
  ToStationName: 0,
  TrainClass: 2,
  searchdate: moment().format('YYYY-MM-DD'),
  FromTimeSelect: moment().format('HHmm'),
  ToTimeSelect: moment().add(1, 'hours').format('HHmm'),
  Timetype: 1
}

var options = {
  url: 'http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx',
  method: 'POST',
  form: data,
}
request(options, (err, res, body)=>{
  var dom = new JSDOM(body, { runScripts: "dangerously" });
  console.log(dom.window.JSONData);
})

