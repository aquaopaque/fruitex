angular.module('store.controllers', [
  'common.resources',
  'store.directives'
])
.controller('FruitexFaq', [
  '$scope', '$q', '$http',
  function($scope, $q, $http) {
    $scope.faq = [];

    $scope.init = function() {
	    $http.get('/static/ng/store/faq.json')
		    .then(function(res) {
			    $scope.faq = res.data;
		    });
    };
  }
]);
