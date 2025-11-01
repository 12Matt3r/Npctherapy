
import { test, expect } from '@playwright/test';

test.describe('NPC Therapy Game - Meta Ending', () => {
  // Increase the timeout for this test as it involves more steps
  test.setTimeout(60000);

  test('should trigger the meta ending after the secret patient session', async ({ page }) => {
    // Navigate to the game page
    await page.goto('http://localhost:8000');

    // Manually trigger the conditions to unlock the secret patient
    await page.evaluate(() => {
        metaStats.fourthWallBreaks = 3;
        metaStats.secretPatientUnlocked = true;
        if (!npcs.find(npc => npc.id === 99)) {
            npcs.push(secretPatient);
        }
        // Set the index to the one before the secret patient.
        currentNPCIndex = npcs.length - 2;
    });

    // Helper function to complete a full session
    const completeFullSession = async () => {
      // Skip initial dialogue
      await page.click('button:has-text("Continue")');

      // Answer all 5 questions to enable the "End Session" button
      for (let i = 0; i < 5; i++) {
        await page.waitForSelector('.question');
        await page.locator('.question').first().click();

        // Wait for animations and state changes
        await page.waitForTimeout(1000);

        // The 'Ask New Questions' button is used to proceed after each question, except the last one
        if (i < 4) {
          await page.click('button:has-text("Ask New Questions")');
        }
      }

      // Now the "End Session" button should be enabled
      await page.click('button:has-text("End Session")');
    };

    // Start the game and go to the first NPC
    await page.click('button:has-text("Begin Therapy Journey")');
    await page.click('button:has-text("Enter Therapy Office →")');

    // Complete the session for the NPC before the secret one
    await completeFullSession();

    // This will take us to the secret patient
    await page.click('button:has-text("Continue to Next Patient →")');

    // Verify we are on the secret patient's session
    await page.waitForSelector('#npcName:has-text("The Previous Therapist")');

    // Complete the secret patient's session
    await completeFullSession();

    // This click should now trigger the meta ending
    await page.click('button:has-text("Continue to Next Patient →")');

    // Verify that the meta ending screen is displayed
    await page.waitForSelector('#metaEnding', { state: 'visible', timeout: 5000 });
    const endingText = await page.textContent('#ending-text-2');
    expect(endingText).toContain('You were not the therapist. You were the patient');
  });
});
