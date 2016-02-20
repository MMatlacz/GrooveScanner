angular.module 'upc'
  .controller 'HomeController', ($scope, $timeout, Event) ->
    'ngInject'

    $scope.search =
      typeahead: []

      query: ''

      debouncer: null
      debounceTypeahead: ->
        if $scope.search.debouncer then do $scope.search.debouncer.cancel

        $scope.search.debouncer = $timeout ->
          $scope.search.typeahead = Event.query($scope.search.query)
          $scope.search.debouncer = null
        , 1000

      submit: ->
        console.log "i am lame ;("

    @
