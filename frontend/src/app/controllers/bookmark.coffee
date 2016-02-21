angular.module 'upc'
  .controller 'BookmarkController', ($scope, $rootScope, $sce, $stateParams, $modal, toastr, Airport, Event, Plan) ->
    'ngInject'

    $rootScope.bgstate = 'high'

    $scope.event = null
    $scope.loading_failed = null

    $scope.modal = (plan) ->
      event = $scope.event

      $modal.open
        templateUrl: 'app/views/bookmark_details.html'
        controller: ($scope) ->
          $scope.plan = plan
          $scope.event = event

    Event.get($stateParams.event_id).$promise.then (event) ->
      $scope.event = event
      url = "https:\/\/www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d11972.733584287987!2d" + \
        event.place.location.longitude + "!3d" + event.place.location.latitude + \
        "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1spl!2ses!4v1456007953889"
      $scope.event_map = $sce.trustAsResourceUrl url

      start_time = event.start_time.split("T")[0]
      end_time = event.end_time.split("T")[0]

      Airport.get($stateParams.airport).$promise.then (airport) ->
        $scope.sourceAirport = airport

        Plan.query(airport.city, airport.country, event.place.location.city, event.place.location.country, \
                    start_time, end_time).$promise.then (data) ->
          $scope.plans = data

    , ->
      $scope.loading_failed = 'Error loading event details. Please try again.'

    @