/**
 * Created by suzukiyosuke on 4/29/15.
 */

var gulp = require('gulp');
var runSequence = require('run-sequence');
var protractor = require('gulp-protractor').protractor;


gulp.task('protractor', function() {
  return gulp
  .src(['./e2e/spec/*.js'])
  .pipe(protractor({
    configFile: './e2e/config.js',
    args: ['--baseUrl', 'http://localhost:8080']
  }))
  .on('error', function(e) { throw e; });
});

gulp.task('test:e2e', function(callback) {
  runSequence(
    'protractor',
    callback
  );
});
