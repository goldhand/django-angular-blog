'use strict';

/* Services */

angular.module('postsServices', ['ngResource']).
    factory('Post', function($resource){
  return $resource('/api/posts/:postId/', {}, {
    query: {method:'GET', params:{postId:''}, isArray:false}
  });
});