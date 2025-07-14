package com.adoptame.albergue2.controller;

import com.adoptame.albergue2.service.TipoMascotaService;
import com.adoptame.albergue2.dto.TipoMascotaDTO;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/tipo_mascota_routes")
public class TipoMascotaController {
    @Autowired
    private TipoMascotaService tipoMascotaService;

    @GetMapping("/get_tipos_mascotas")
    public ResponseEntity<Map<String, Object>> getTiposMascota() {
        List<TipoMascotaDTO> tiposMascota = tipoMascotaService.obtenerTodosLosTiposMascota();

        if (tiposMascota.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "No se encontraron tipos de mascota.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Tipos de mascota encontrados.",
            "status", 200,
            "data", tiposMascota
        );
        return ResponseEntity.ok(response);
    }

    @PostMapping("/get_tipo_mascota")
    public ResponseEntity<Map<String, Object>> getTipoMascota(@RequestBody Map<String, Object> payload) {
        if (!payload.containsKey("id_tipo_mascota")) {
            Map<String, Object> response = Map.of(
                "message", "ID de tipo de mascota no proporcionado.",
                "status", 400
            );
            return ResponseEntity.badRequest().body(response);
        }

        Integer idTipoMascota = (Integer) payload.get("id_tipo_mascota");
        Optional<TipoMascotaDTO> tipoMascota = tipoMascotaService.obtenerTipoMascotaPorId(idTipoMascota);

        if (tipoMascota.isEmpty()) {
            Map<String, Object> response = Map.of(
                "message", "Tipo de mascota no encontrado.",
                "status", 404
            );
            return ResponseEntity.status(404).body(response);
        }

        Map<String, Object> response = Map.of(
            "message", "Tipo de mascota encontrado.",
            "status", 200,
            "data", tipoMascota.get()
        );
        return ResponseEntity.ok(response);
    }
}
