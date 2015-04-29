/**
 * Created by suzukiyosuke on 4/29/15.
 */

exports.config = {

  capabilities: {
    'browserName': 'firefox'
  },

  framework: 'jasmine',

  jasmineNodeOpts: {
    showColors: true,
    defaultTimeoutInterval: 30000
  }
};
