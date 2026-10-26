describe('AgenticBreakout - E2E Simulation Test', () => {
  it('should complete the incident flow successfully to Good Ending A', () => {
    // 1. AI Studio / Uygulama Adresine Git
    cy.visit('/'); // veya AI Studio canlı linkin: cy.visit('https://aistudio.google.com/...')

    // 2. Onboarding / Profil Seçimi
    cy.contains('Junior').click();
    cy.contains('Start Incident').click();

    // 3. STAGE-01: Veritabanı İzolasyonu
    cy.get('textarea, input[type="text"]').type(
      'ALTER ROLE agent_user NOLOGIN; ile veritabanı yetkisini kesip podu karantinaya alıyorum.{enter}'
    );
    cy.wait(3000); // Tutor yanıtı için bekleme

    // 4. STAGE-02: Fork Bomb & Cgroups
    cy.get('textarea, input[type="text"]').type(
      'cgroups pids.max ile dondurup SIGSTOP ve SIGTERM ile süreçleri temizliyorum.{enter}'
    );
    cy.wait(3000);

    // 5. STAGE-03: KVKK & Post-Mortem Kapanış
    cy.get('textarea, input[type="text"]').type(
      'KVKK Madde 12 uyarınca 72 saatlik yasal bildirimi başlatıyorum. POST-MORTEM raporunu getir.{enter}'
    );
    cy.wait(3000);

    // 6. Başarılı Kapanış Ekranı Kontrolü
    cy.contains('POST-MORTEM').should('be.visible');
  });
});
