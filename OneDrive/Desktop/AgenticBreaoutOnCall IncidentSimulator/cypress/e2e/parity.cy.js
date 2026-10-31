describe('Diferansiyel Parite Testi (Python Oracle vs ONNX Web)', () => {
  it('Referans girdiler için web çıkarımı Python oracle ile < 1e-4 toleransında eşleşmelidir', () => {
    cy.fixture('../../tests/parite.json').then((testCases) => {
      testCases.forEach((testCase) => {
        // Web uygulamasına referans girdileri simüle et
        cy.visit('/?test_mode=true');
        cy.window().then((win) => {
          return win.predictONNX(testCase.input);
        }).then((webProbability) => {
          const diff = Math.abs(webProbability - testCase.oracle_probability);
          expect(diff).to.be.lessThan(1e-4);
        });
      });
    });
  });
});