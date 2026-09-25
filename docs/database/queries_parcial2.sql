SELECT 
    t.id AS ticket_id,
    t.title,
    t.status,
    u.name AS requester_name
FROM tickets t
JOIN users u ON t.requester_id = u.id
WHERE t.status = 'open';

-- Consulta b) Conteo de tickets por técnico asignado (HAVING > 0 y ORDER BY DESC)
SELECT 
    u.id AS technician_id,
    u.name AS technician_name,
    COUNT(t.id) AS total_tickets
FROM users u
JOIN tickets t ON u.id = t.assignee_id
GROUP BY u.id, u.name
HAVING COUNT(t.id) > 0
ORDER BY total_tickets DESC;

-- Consulta c) Tickets sin comentarios mediante NOT EXISTS
SELECT 
    t.id,
    t.title,
    t.status
FROM tickets t
WHERE NOT EXISTS (
    SELECT 1 
    FROM comments c 
    WHERE c.ticket_id = t.id
);

-- Consulta d) Demostración de ON DELETE CASCADE sobre el historial en transacción
BEGIN;

-- 1. Verificación del conteo inicial en la tabla history_events
SELECT COUNT(*) AS conteo_inicial 
FROM history_events 
WHERE ticket_id = 1;

-- 2. Borrado del ticket
DELETE FROM tickets 
WHERE id = 1;

-- 3. Verificación de borrado en cascada (debe retornar 0)
SELECT COUNT(*) AS conteo_tras_delete 
FROM history_events 
WHERE ticket_id = 1;

-- 4. Reversión para conservar los datos intactos
ROLLBACK;

-- 5. Verificación de restauración del conteo original
SELECT COUNT(*) AS conteo_tras_rollback 
FROM history_events 
WHERE ticket_id = 1;