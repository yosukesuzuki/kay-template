/**
 * Created by suzukiyosuke on 4/29/15.
 */

describe('gulp-protractor-sample', function() {

  beforeEach(function() {
    browser.ignoreSynchronization = true;
    browser.get(browser.baseUrl);
  });

  it('Title', function() {
    expect($('h1').getText()).toBe('Kay Template');
  });

});
