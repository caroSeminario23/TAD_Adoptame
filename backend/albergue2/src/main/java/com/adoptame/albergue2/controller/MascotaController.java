package com.adoptame.albergue2.controller;

import com.adoptame.albergue2.model.Mascota;
import com.adoptame.albergue2.service.MascotaService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/mascota_routes")
public class MascotaController {
    @Autowired
    private MascotaService mascotaService;

    @GetMapping("/get_mascotas")
    public ResponseEntity<Map<String, Object>> getMascotas() {
        List<Mascota> mascotas = mascotaService.obtenerTodasLasMascotas();

        if (mascotas.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "No se encontraron mascotas.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Mascotas encontradas.",
            "status", 200,
            "data", mascotas
        );
        return ResponseEntity.ok(response);
    }

    @PostMapping("/get_mascota")
    public ResponseEntity<Map<String, Object>> getMascota(@RequestBody Map<String, Object> payload) {
        if (!payload.containsKey("id_mascota")) {
            Map<String, Object> response = Map.of(
                "message", "ID de mascota no proporcionado.",
                "status", 400
            );
            return ResponseEntity.badRequest().body(response);
        }

        Integer idMascota = (Integer) payload.get("id_mascota");
        Optional<Mascota> mascota = mascotaService.obtenerMascotaPorId(idMascota);

        if (mascota.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "Mascota no encontrada.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Mascota encontrada.",
            "status", 200,
            "data", mascota.get()
        );
        return ResponseEntity.ok(response);
    }
}
