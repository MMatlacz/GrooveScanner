angular.module 'upc'
  .config ($stateProvider, $urlRouterProvider) ->
    'ngInject'
    $stateProvider
      .state 'home',
        url: '/'
        templateUrl: 'app/views/home.html'
        controller: 'HomeController'

      .state 'search',
        url: '/search/:query'
        templateUrl: 'app/views/search.html'
        controller: 'SearchController'

      .state 'event',
        url: '/event/:id'
        templateUrl: 'app/views/event.html'
        controller: 'EventController'

      .state 'bookmark',
        url: '/bookmark/:id'
        templateUrl: 'app/views/bookmark.html'
        controller: 'BookmarkController'

    $urlRouterProvider.otherwise '/'
