'use strict';

/* Controllers */

function PostListCtrl($scope, $routeParams, $location, $http, $sce, Post) {
    $scope.posts = Post.query(function (posts) {
        for (var i=0; i < posts.results.length; i++) {
            $scope.posts.results[i].content = $sce.trustAsHtml(posts.results[i].content);

        }

    });

    $scope.updateUrl = function (postId) {
        $location.path('posts/' + postId);
    };
    $scope.getPosts = function (url) {
        $http.get(url).success(function(data) {
            $scope.posts = data;
        });
    };
    $scope.appendPosts = function (url) {
        if (!(url === null)) {

        $http.get(url).success(function(data) {
            for (var i=0; i < data.results.length; i++) {
                data.results[i].content = $sce.trustAsHtml(data.results[i].content);
            }
            $scope.posts.results = $scope.posts.results.concat(data.results);

                $scope.posts.next = data.next;
        });
        }
    };
    $scope.orderProp = 'created';
}

//PhoneListCtrl.$inject = ['$scope', '$http'];


function PostDetailCtrl($scope, $routeParams, $http, $sce, Post) {
    // Note: this error "http://docs.angularjs.org/error/$rootScope:infdig" was fixed by making postContent a variable
    // instead of a function
    $scope.post = Post.get({postId: $routeParams.postId}, function (post) {
        $scope.postContent =  $sce.trustAsHtml(post.content);
//        $http.get(post.owner).success(function(data) {
//            $scope.postAuthor = data.username;
//        });
    });
    $scope.orderProp = 'created';
}

//PhoneDetailCtrl.$inject = ['$scope', '$routeParams'];

function AuthorCtrl($scope, $http) {
    $http.get('/static/author/author.json').success(function(data) {
        $scope.author = data;
    });
}


