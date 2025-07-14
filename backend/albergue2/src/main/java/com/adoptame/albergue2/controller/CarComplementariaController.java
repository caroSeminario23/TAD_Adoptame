package com.adoptame.albergue2.controller;

import com.adoptame.albergue2.model.CaracteristicaComplementaria;
import com.adoptame.albergue2.service.CarComplementariaService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/car_complementaria_routes")
public class CarComplementariaController {
    @Autowired
    private CarComplementariaService carComplementariaService;

    @GetMapping("/get_caracteristicas_complementarias")
    public ResponseEntity<Map<String, Object>> getCaracteristicasComplementarias() {
        List<CaracteristicaComplementaria> caracteristicas = carComplementariaService.obtenerTodasLasCaracteristicasComplementarias();

        if (caracteristicas.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "No se encontraron características complementarias.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Características complementarias encontradas.",
            "status", 200,
            "data", caracteristicas
        );
        return ResponseEntity.ok(response);
    }

    @PostMapping("/get_caracteristica_complementaria")
    public ResponseEntity<Map<String, Object>> getCaracteristicaComplementaria(@RequestBody Map<String, Object> payload) {
        if (!payload.containsKey("id_caracteristica_complementaria")) {
            Map<String, Object> response = Map.of(
                "message", "ID de característica complementaria no proporcionado.",
                "status", 400
            );
            return ResponseEntity.badRequest().body(response);
        }

        Integer idCaracteristica = (Integer) payload.get("id_caracteristica_complementaria");
        Optional<CaracteristicaComplementaria> caracteristica = carComplementariaService.obtenerCaracteristicaComplementariaPorId(idCaracteristica);

        if (caracteristica.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "Característica complementaria no encontrada.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Característica complementaria encontrada.",
            "status", 200,
            "data", caracteristica.get()
        );
        return ResponseEntity.ok(response);
    }
}
