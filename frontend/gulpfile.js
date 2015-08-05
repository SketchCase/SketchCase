var gulp = require('gulp');
var browserify = require('gulp-browserify');
var sass = require('gulp-sass');

gulp.task('scripts', function () {
	gulp.src('js/main.js')
		.pipe(browserify({
			transform: ['babelify']
		}))
		.pipe(gulp.dest('static/'));
});

gulp.task('sass', function () {
	gulp.src('sass/main.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(gulp.dest('static/'));
});

gulp.task('watch', function () {
	gulp.watch('sass/**/*.scss', ['sass']);
	gulp.watch('js/**/*.js', ['scripts']);
});