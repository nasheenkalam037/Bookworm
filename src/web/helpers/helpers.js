var dateFormat = require('dateformat');
var _relativeDate = require('relative-date');
module.exports = {
    ifeq: function(a, b, options){
      if (a === b) {
        return options.fn(this);
        }
      return options.inverse(this);
    },
    bar: function(){
      return "BAR!";
    },
    escapeQuotes: function(variable){
      return variable.replace(/(['"])/g, '\\$1');;
    },
    formatDate: function(date) {
      return dateFormat(date, "ddd, mmm dS, yyyy, h:MM:ss TT");
    },
    relativeDate: function(date) {
      return _relativeDate(date);
    },
    urlencode: function(text) {
      return encodeURIComponent(text.replace("'", ''));
    }
  }