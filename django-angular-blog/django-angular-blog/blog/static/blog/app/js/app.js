'use strict';

/* App Module */

//noinspection JSValidateTypes
angular.module('posts', ['postsServices', 'ngRoute', 'ngAnimate']).

  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/posts', {templateUrl: '/api/angular/partials/post-list/'}).
      when('/posts/:postId', {templateUrl: '/api/angular/partials/post-detail/'}).
      otherwise({redirectTo: '/posts'});
    }])
;


