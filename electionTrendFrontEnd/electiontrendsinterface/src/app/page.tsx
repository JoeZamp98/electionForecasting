"use client"

import react, { useState } from 'react';
import { useRouter } from 'next/navigation';
import styles from '../app/homepage.module.css';
import Image from 'next/image';
import '../styles/globals.css'


const HomePage = () => {
  
  const router = useRouter();

  const handleNavigation = (path: string) => {
    router.push(path)
  };

  return (
    <div>
      <div className={styles.welcomeBlock}>
        <h1 className={styles.welcomeLine}>Welcome to The United States Partisan Trends Explorer</h1>
        {/* <Image
                    src="/images/Logo.png"
                    alt="Description of the image"
                    width={100}
                    height={30}
        /> */}
      </div>

      
      <div className={styles.pathSelectionBlock}>
        <button className={styles.pathSelectionButton} onClick={() => handleNavigation('/geographicExplorer')}>
          <p className={styles.pathSelectionButtonHeader}>Tool 1: Geographic Explorer</p>
          <p className={styles.pathSelectionButtonSubtext}>Additional Detail Here</p>
        </button>
        <button className={styles.pathSelectionButton} onClick={() => handleNavigation('/partisanLean')}>
          <p className={styles.pathSelectionButtonHeader}>Tool 2: Partisan Lean Directory</p>
          <p className={styles.pathSelectionButtonSubtext}>Additional Detail Here</p>
        </button>
        <button className={styles.pathSelectionButton} onClick={() => handleNavigation('/trendOverTime')}>
          <p className={styles.pathSelectionButtonHeader}>Tool 3: Trends Over Time</p>
          <p className={styles.pathSelectionButtonSubtext}>Additional Detail Here</p>
        </button>
      </div>
      </div>
  );
};

export default HomePage;
