'use strict';

/* App Module */
angular.module('HashBangURLs', []).config(['$locationProvider', function($location) {
  $location.hashPrefix('!');
}]);

//noinspection JSValidateTypes
angular.module('posts', ['postsServices', 'ngRoute', 'ngAnimate', 'HashBangURLs']).

  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/posts', {templateUrl: '/api/angular/partials/post-list/'}).
      when('/posts/:postId', {templateUrl: '/api/angular/partials/post-detail/'}).
      otherwise({redirectTo: '/posts'});
    }])
;


