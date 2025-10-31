
import { test, expect } from '@playwright/test';

test.describe('NPC Therapy Game - Dynamic Atmosphere', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the game page
    await page.goto('http://localhost:8000');
    // Start the game and enter the therapy office for the first NPC
    await page.click('button:has-text("Begin Therapy Journey")');
    await page.click('button:has-text("Enter Therapy Office →")');
    // Skip the initial dialogue to get to the questions
    await page.click('button:has-text("Continue")');
  });

  test('should apply "atmosphere-hopeful" class when hope is high', async ({ page }) => {
    // Click the question that gives a big boost to 'hope'
    await page.click('.question:has-text("What truth about yourself are you most afraid to speak aloud?")');

    // The emotional state update is animated, so wait a bit for the class to be applied
    await page.waitForTimeout(500);

    const officeBg = await page.locator('.therapy-office-bg');
    await expect(officeBg).toHaveClass(/atmosphere-hopeful/);
  });

  test('should apply "atmosphere-enraged" class when rage is high', async ({ page }) => {
    // This question should increase rage.
    await page.click('.question:has-text("When the world moves on without you, where do you find yourself?")');
    await page.waitForTimeout(500);

    const officeBg = await page.locator('.therapy-office-bg');
    await expect(officeBg).toHaveClass(/atmosphere-enraged/);
  });

  test('should apply "atmosphere-serene" class when acceptance is high', async ({ page }) => {
    // Click a question that boosts acceptance.
    await page.click('.question:has-text("What would you say to the version of yourself who first felt broken?")');
    await page.waitForTimeout(500);

    const officeBg = await page.locator('.therapy-office-bg');
    await expect(officeBg).toHaveClass(/atmosphere-serene/);
  });
});
