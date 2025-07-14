package com.adoptame.albergue2.controller;

import com.adoptame.albergue2.model.CaracteristicaMascota;
import com.adoptame.albergue2.service.CarMascotaService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/car_mascota_routes")
public class CarMascotaController {
    @Autowired
    private CarMascotaService carMascotaService;

    @GetMapping("/get_caracteristicas_mascota")
    public ResponseEntity<Map<String, Object>> getCaracteristicasMascota() {
        List<CaracteristicaMascota> caracteristicas = carMascotaService.obtenerTodasLasCaracteristicasMascota();

        if (caracteristicas.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "No se encontraron características de mascota.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Características de mascota encontradas.",
            "status", 200,
            "data", caracteristicas
        );
        return ResponseEntity.ok(response);
    }

    @PostMapping("/get_caracteristica_mascota")
    public ResponseEntity<Map<String, Object>> getCaracteristicaMascota(@RequestBody Map<String, Object> payload) {
        if (!payload.containsKey("id_mascota") || !payload.containsKey("id_caracteristica")) {
            Map<String, Object> response = Map.of(
                "message", "ID de mascota o de característica complementaria no proporcionado.",
                "status", 400
            );
            return ResponseEntity.badRequest().body(response);
        }

        Integer idMascota = (Integer) payload.get("id_mascota");
        Integer idCaracteristica = (Integer) payload.get("id_caracteristica");
        Optional<CaracteristicaMascota> caracteristica = carMascotaService.obtenerCaracteristicaMascotaPorId(idMascota, idCaracteristica);

        if (caracteristica.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "Característica de mascota no encontrada.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Característica de mascota encontrada.",
            "status", 200,
            "data", caracteristica.get()
        );
        return ResponseEntity.ok(response);
    }
}
