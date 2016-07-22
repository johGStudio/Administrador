var app = angular.module("app",["ngResource"]);

app.factory("materia",function($resource){
	//return $resource(url,paramDefaults, actions)
	return $resource(
		"http://127.0.0.1:8001/servicioWeb/materia/",
		{},
		{get:{method:"GET",isArray:true}});
 });

app.factory("estudiante",function($resource){
	//return $resource(url,paramDefaults, actions)
	return $resource(
		"http://127.0.0.1:8001/servicioWeb/alumno/",
		{},
		{get:{method:"GET",isArray:true}});
 });

app.controller("controlador13",function($scope,materia,estudiante){
	$scope.mater= materia.get();
	$scope.lista2= estudiante.get();
	$scope.foco=false;
	$scope.mensaje="";

	$scope.ingresar = function(){
		var id=$scope.cedulaEntrada;
		var band=true;
		for (var i=0; i < $scope.lista2.length; i++) {
			if(id == $scope.lista2[i].cedula){
				band=false;
				break;
			}
		}
		if(band==false){
			$scope.foco=true;
		}
		else{
			$scope.mensaje="No se encuentra el estudiante";
		}
	}
	$scope.mensaje = function(){
		alert("Matricula Solicitada Con Éxito");
	}
});




