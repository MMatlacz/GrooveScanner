angular.module 'upc'
  .controller 'HomeController', ($scope, $timeout, $geolocation, toastr, Airport, Event) ->
    'ngInject'

    $geolocation.getCurrentPosition({timeout: 60000}).then (position) ->
      console.log position

    $scope.search =
      typeahead: []

      query: ''
      airport: null
      airports: Airport.query()

      loading: false
      search: (query) ->
        return Event.query(query).$promise.then (data) ->
          return data

      submit: ->
        if not $scope.search.airport or not $scope.search.event
          toastr.error 'You must input starting airport and event you want to go on.'

    @
