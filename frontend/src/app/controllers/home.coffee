angular.module 'upc'
  .controller 'HomeController', ($scope, $timeout, Event) ->
    'ngInject'

    $scope.search =
      typeahead: []

      query: ''

      loading: false
      search: (query) ->
        return Event.query(query).$promise.then (data) ->
          return data


      submit: ->
        console.log "i am lame ;("

    @
